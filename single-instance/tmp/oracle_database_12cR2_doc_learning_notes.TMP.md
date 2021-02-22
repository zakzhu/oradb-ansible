- Oracle Database Installation Checklist
  https://docs.oracle.com/en/database/oracle/oracle-database/12.2/ladbi/oracle-database-installation-checklist.html#GUID-E847221C-1406-4B6D-8666-479DB6BDB046

  - 1 ok

    > - At least 1 GB RAM for Oracle Database installations. 2 GB RAM recommended.
    > - At least 8 GB RAM for Oracle Grid Infrastructure installations.

  - 2 ok

  - 3 ok

    > The OINSTALL group must be the primary group of all Oracle software installation owners on the server. It should be writable by any Oracle installation owner. 
    >
  > ---
  >
  > Mount point paths for the software binaries
  >
  > Oracle recommends that you create an Optimal Flexible Architecture configuration as described in the appendix "Optimal Flexible Architecture" in *Oracle Database Installation Guide* for your platform.
  >
  > ---
  >
  > Unset Oracle software environment variables
  >
  > If you have an existing Oracle software installation, and you are using the same user to install this installation, then unset the following environment variables: `$ORACLE_HOME`,`$ORA_NLS10`, and `$TNS_ADMIN`.
  >
  > If you have set `$ORA_CRS_HOME` as an environment variable, then unset it before starting an installation or upgrade. Do not use `$ORA_CRS_HOME` as a user environment variable, except as directed by Oracle Support.
  >
  > If you have had an existing installation on your system, and you are using the same user account to install this installation, then unset the ORACLE_HOME, ORACLE_BASE, ORACLE_SID, TNS_ADMIN environment variables and any other environment variable set for the Oracle installation user that is connected with Oracle software homes. 
  >
  > 
  
  - 4 ok
  
    > Review Oracle Inventory (oraInventory) and OINSTALL Group Requirements 
    >
    > The physical group you designate as the Oracle Inventory directory is the central inventory of Oracle software installed on your system. It should be the primary group for all Oracle software installation owners. Users who have the Oracle Inventory group as their primary group are granted the OINSTALL privilege to read and write to the central inventory.
    >
    > - If you have an existing installation, then OUI detects the existing oraInventory directory from the`/etc/oraInst.loc` file, and uses this location.
    > - If you are installing Oracle software for the first time, then OUI creates an Oracle base and central inventory, and creates an Oracle inventory using information in the following priority:
    >   - In the path indicated in the ORACLE_BASE environment variable set for the installation owner user account.
    >   - In an Optimal Flexible Architecture (OFA) path (u[01–99]/app/*owner* where *owner* is the name of the user account running the installation), if that user account has permissions to write to that path.
    >   - In the user home directory, in the path /app/*owner*, where *owner* is the name of the user account running the installation.
    >
    > Ensure that the group designated as the OINSTALL group is available as the primary group for all planned Oracle software installation owners.
  
  - 5 ok
  
  - 6 ok
  
    > Ensure `cron` jobs do not run during installation
    >
    > If the installer is running when daily cron jobs start, then you may encounter unexplained installation problems if your cron job is performing cleanup, and temporary files are deleted before the installation is finished. Oracle recommends that you complete installation before daily cron jobs are run, or disable daily cron jobs that perform cleanup until after the installation is completed.
    >
    > ---
    >
    > Review memory allocation and Automatic Memory Management feature
    >
    > You can enable automatic memory management either during, or after Oracle Database installation. If you enable automatic memory management after installation, then you must shut down and restart the database.
    >
    > If the total physical memory of your database instance is greater than 4 GB, then you cannot select the Oracle Automatic Memory Management option during database installation and creation. Instead, use automatic shared memory management. Automatic shared memory management automatically distributes the available memory among the various components as required, allowing the system to maximize the use of all available SGA memory.
    >
    > For more information, see:
    >
    > [*Oracle Database Administrator's Guide*](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/ladbi&id=ADMIN11011)
  
- Checking Server Hardware and Memory Configuration
https://docs.oracle.com/en/database/oracle/oracle-database/12.2/ladbi/checking-server-hardware-and-memory-configuration.html#GUID-DC04ABB6-1822-444A-AB1B-8C306079439C

- Oracle Linux packages on the Oracle Linux yum server website:
http://yum.oracle.com/repo/OracleLinux/OL7/latest/x86_64/

- When installed, the Oracle Preinstallation RPM does the following:

Automatically downloads and installs any additional RPM packages needed for installing Oracle Grid Infrastructure and Oracle Database, and resolves any dependencies

Creates an oracle user, and creates the oraInventory (oinstall) and OSDBA (dba) groups for that user

As needed, sets sysctl.conf settings, system startup parameters, and driver parameters to values based on recommendations from the Oracle RDBMS Pre-Install program

Sets hard and soft resource limits

Sets other recommended parameters, depending on your kernel version

- Restrictions for HugePages and Transparent HugePages Configurations
https://docs.oracle.com/en/database/oracle/oracle-database/12.2/ladbi/restrictions-for-hugepages-and-transparent-hugepages-configurations.html#GUID-D8178896-D00F-4F02-82A7-A44F89D8F103

Oracle recommends that you disable Transparent HugePages, because they may cause delays in accessing memory that can result in node restarts in Oracle RAC environments, or performance issues or delays for Oracle Database single instances. Oracle continues to recommend using standard HugePages for Linux.

- Supported Red Hat Enterprise Linux 7 Distributions for x86-64
https://docs.oracle.com/en/database/oracle/oracle-database/12.2/ladbi/supported-red-hat-enterprise-linux-7-distributions-for-x86-64.html#GUID-2E11B561-6587-4789-A583-2E33D705E498

- Installation Requirements for Programming Environments for Linux x86-64
https://docs.oracle.com/en/database/oracle/oracle-database/12.2/ladbi/installation-requirements-for-programming-environments-for-linux-x86-64.html#GUID-BFD716A4-6235-49F6-8259-A534E2D96A8D

- Checking Kernel and Package Requirements for Linux
https://docs.oracle.com/en/database/oracle/oracle-database/12.2/ladbi/checking-kernel-and-package-requirements-for-linux.html#GUID-7065A86D-C2AB-4731-953B-12AC25C94156

- Confirming Host Name Resolution
https://docs.oracle.com/en/database/oracle/oracle-database/12.2/ladbi/confirming-host-name-resolution.html#GUID-B12E885F-CF2E-498A-A878-117082F237CC

- Disabling Transparent HugePages
https://docs.oracle.com/en/database/oracle/oracle-database/12.2/ladbi/disabling-transparent-hugepages.html#GUID-02E9147D-D565-4AF8-B12A-8E6E9F74BEEA

- Using Automatic SSH Configuration During Installation
https://docs.oracle.com/en/database/oracle/oracle-database/12.2/ladbi/using-automatic-ssh-configuration-during-installation.html#GUID-51280BE9-4B2A-4BE3-9DA3-68B795D9FBA2

- Verifying the Disk I/O Scheduler on Linux
https://docs.oracle.com/en/database/oracle/oracle-database/12.2/ladbi/setting-the-disk-io-scheduler-on-linux.html#GUID-B59FCEFB-20F9-4E64-8155-7A61B38D8CDF

- 5 Configuring Users, Groups and Environments for Oracle Grid Infrastructure and Oracle Database
https://docs.oracle.com/en/database/oracle/oracle-database/12.2/ladbi/configuring-users-groups-and-environments-for-oracle-grid-infrastructure-and-oracle-database.html#GUID-B65E6113-D056-4DD9-940F-DFF493E413D5

MARK: Creating Operating System Oracle Installation User Accounts

- About Automatic Memory Management Installation Options
https://docs.oracle.com/en/database/oracle/oracle-database/12.2/ladbi/about-automatic-memory-management-installation-options.html#GUID-38F46564-B167-4A78-A974-8C7CEE34EDFE

- Configuring Kernel Parameters for Linux
https://docs.oracle.com/en/database/oracle/oracle-database/12.2/ladbi/configuring-kernel-parameters-for-linux.html#GUID-6127884D-FB27-45FA-9498-B2540632CBD5

- B Installing and Configuring Oracle Database Using Response Files
https://docs.oracle.com/en/database/oracle/oracle-database/12.2/ladbi/installing-and-configuring-oracle-database-using-response-files.html#GUID-D53355E9-E901-4224-9A2A-B882070EDDF7

- C Optimal Flexible Architecture
https://docs.oracle.com/en/database/oracle/oracle-database/12.2/ladbi/optimal-flexible-architecture.html#GUID-34434C8B-EBEE-497A-BB92-26B43561B6B1
