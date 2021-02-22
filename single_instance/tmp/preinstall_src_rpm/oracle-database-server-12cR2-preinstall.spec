%define name oracle-database-server-12cR2-preinstall 
%define version 1.0
%define release 5%{?dist}

Summary: Sets the system for Oracle Database single instance and Real Application Cluster install for Oracle Linux 7
Name: %{name}
Version: %{version}
Release: %{release}
Group: Test Environment/Libraries
License: GPLv2
Vendor:Oracle
Source: %{name}-%{version}.tar.gz

Patch1:bug28058876.patch
Patch2:bug28058890.patch
Patch3:bug29472111.patch

Provides: %{name} = %{version}

Requires(pre):/etc/redhat-release

#System requirement
Requires:procps module-init-tools ethtool initscripts 
Requires:bind-utils nfs-utils util-linux-ng pam
Requires:xorg-x11-utils xorg-x11-xauth 
Requires:kernel-uek
Requires:smartmontools

#As per docs
Requires:binutils compat-libstdc++-33 glibc glibc-devel 
Requires:ksh libaio libaio-devel libgcc libstdc++ libstdc++-devel 
Requires:make sysstat openssh-clients compat-libcap1 

#As per Orabug 20063241, 22250148, 22829306
Requires:psmisc net-tools unzip oraclelinux-release

BuildRoot: %{_builddir}/%{name}-%{version}-root

%description
The Oracle Preinstallation RPM package installs software packages and sets system parameters required for Oracle Database single instance and Oracle Real Application Clusters installations version 12cR2 on Oracle Linux Release 7
Files affected: /etc/sysctl.conf, /boot/grub/menu.lst OR /boot/grub2/grub.cfg 
Files added: /etc/security/limits.d/%{name}.conf


%prep
echo RPM_BUILD_ROOT=$RPM_BUILD_ROOT
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p -m 755 $RPM_BUILD_ROOT/etc/sysconfig/%{name}
mkdir -p -m 755 $RPM_BUILD_ROOT/usr/bin
mkdir -p -m 755 $RPM_BUILD_ROOT/etc/rc.d/init.d
mkdir -p -m 755 $RPM_BUILD_ROOT/etc/security/limits.d
mkdir -p -m 700 $RPM_BUILD_ROOT/var/log/%{name}/results

install -m 700 %{name}-verify $RPM_BUILD_ROOT/etc/sysconfig/%{name}
install -m 700 %{name}-verify $RPM_BUILD_ROOT/usr/bin
install -m 600 %{name}.param $RPM_BUILD_ROOT/etc/sysconfig/%{name}
install -m 700 %{name}-firstboot $RPM_BUILD_ROOT/etc/rc.d/init.d
touch $RPM_BUILD_ROOT/etc/security/limits.d/%{name}.conf


ln -f -s /etc/sysconfig/%{name}/%{name}-verify $RPM_BUILD_ROOT/usr/bin/%{name}-verify 

%clean
rm -rf $RPM_BUILD_ROOT

%pre

if [ -f  /etc/sysconfig/%{name}/%{name}.param ]; then 
  cp -f /etc/sysconfig/%{name}/%{name}.param /var/log/%{name}/results/.%{name}.param 
fi

if [ -d /etc/sysconfig/%{name} ]; then
  rm -rf /etc/sysconfig/%{name} 
fi	

%preun
if [ "$1" = "0" ] ; then # last uninstall
 chkconfig --del %{name}-firstboot
 if [ -x /usr/bin/%{name}-verify ]; then
   /usr/bin/%{name}-verify -u 2> /dev/null 1>&2
 fi
fi

%posttrans
/usr/bin/%{name}-verify 2>/dev/null 1>&2
if ! [ -f /etc/sysconfig/%{name}/%{name}.conf ]; then
  chkconfig --add %{name}-firstboot
fi

%postun
if [ "$1" = "0" ] ; then # last uninstall
 if [ -d /etc/sysconfig/%{name} ]; then
   rm -rf /etc/sysconfig/%{name} 
 fi
 if [ -d /var/log/%{name} ]; then	
   rm -rf /var/log/%{name} 	
 fi
fi

%files
%defattr(-,root,root)
%config /etc/sysconfig/%{name}/%{name}.param
%ghost /etc/security/limits.d/%{name}.conf
/etc/sysconfig/%{name}
/etc/rc.d/init.d/%{name}-firstboot
/etc/sysconfig/%{name}/%{name}-verify  
/var/log/%{name}
/usr/bin/%{name}-verify

%changelog
* Mon Jun 3 2019 Vasundhara V <vasundhara.venkatasubramanian@oracle.com> [1.0-5.el7]
 - Look for exact match in /etc/group [Orabug: 29472111]

* Thu Aug 2 2018 Vasundhara V <vasundhara.venkatasubramanian@oracle.com> [1.0-4.el7]
 - Remove comments from previous preinstall rpm [Orabug: 28058876]
 - Ensure yum erase restores the values of recently installed preinstall rpm [Orabug: 28058890]

* Fri Jun 9 2017 Vasundhara V <vasundhara.venkatasubramanian@oracle.com> [1.0-3.el7]
 - Added new user/groups [Orabug: 25045020]
 - Fix upgrade issues [Orabug: 26244431]
 - Added oraclelinux-release to dependencies [Orabug: 26244588]

* Tue Oct 18 2016 Vasundhara V <vasundhara.venkatasubramanian@oracle.com> [1.0-2.el7]
 - Fixed grub2 entries [Orabug: 24828130]
 - Fixed co-exist issues with sysconfig/network [Orabug: 24903029]
 - Fixed upgrade issues [Orabug: 24903070]

* Tue Aug 17 2016  Vasundhara V <vasundhara.venkatasubramanian@oracle.com> [1.0-1.el7]
 - Initial version with new name
