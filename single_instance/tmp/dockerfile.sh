#!/bin/bash

copy setupLinuxEnv.sh checkSpace.sh /opt/install/

copy runOracle.sh startDB.sh createDB.sh dbca.rsp.tmpl setPassword.sh checkDBStatus.sh runUserScripts.sh /opt/oracle/

chmod ug+x /opt/install/*.sh && \
      sync && \
      # check disk > 15G
      /opt/install/checkSpace.sh && \
      /opt/install/setupLinuxEnv.sh && \
      rm -rf /opt/install

# setupLinuxEnv.sh

ORACLE_BASE=/opt/oracle
ORACLE_HOME=/opt/oracle/product/12.2.0.1/dbhome_1
mkdir -p $ORACLE_BASE/scripts/setup && \
mkdir $ORACLE_BASE/scripts/startup && \
ln -s $ORACLE_BASE/scripts /docker-entrypoint-initdb.d && \
mkdir $ORACLE_BASE/oradata && \

mkdir -p $ORACLE_HOME && \
chmod ug+x /opt/oracle/*.sh && \
yum -y install oracle-database-server-12cR2-preinstall openssl && \
rm -rf /var/cache/yum && \
ln -s /opt/oracle/setPassword.sh /home/oracle/ && \
echo oracle:oracle | chpasswd && \
chown -R oracle:dba /opt/oracle

#COPY --chown=oracle:dba $INSTALL_FILE_1 $INSTALL_RSP $INSTALL_DB_BINARIES_FILE $INSTALL_DIR/
copy --chown=oracle:dba linuxx64_12201_database.zip db_inst.rsp installDBBinaries.sh /opt/install/

su - oracle
chmod ug+x /opt/install/*.sh && \
      sync && \
      /opt/install/installDBBinaries.sh $DB_EDITION

#installDBBinaries.sh
cd $INSTALL_DIR       && \
unzip $INSTALL_FILE_1 && \
rm $INSTALL_FILE_1    && \
$INSTALL_DIR/database/runInstaller -silent -force -waitforcompletion -responsefile $INSTALL_DIR/$INSTALL_RSP -ignoresysprereqs -ignoreprereq && \

cd $HOME
# Remove not needed components
# APEX
rm -rf $ORACLE_HOME/apex && \
# ORDS
rm -rf $ORACLE_HOME/ords && \
# SQL Developer
rm -rf $ORACLE_HOME/sqldeveloper && \
# UCP connection pool
rm -rf $ORACLE_HOME/ucp && \
# All installer files
rm -rf $ORACLE_HOME/lib/*.zip && \
# OUI backup
rm -rf $ORACLE_HOME/inventory/backup/* && \
# Network tools help
rm -rf $ORACLE_HOME/network/tools/help && \
# Database upgrade assistant
rm -rf $ORACLE_HOME/assistants/dbua && \
# Database migration assistant
rm -rf $ORACLE_HOME/dmu && \
# Remove pilot workflow installer
rm -rf $ORACLE_HOME/install/pilot && \
# Support tools
rm -rf $ORACLE_HOME/suptools && \
# Temp location
rm -rf /tmp/* && \
# Database files directory
rm -rf $INSTALL_DIR/database

su - root
$ORACLE_BASE/oraInventory/orainstRoot.sh && \
    $ORACLE_HOME/root.sh


su - oracle
cd /home/oracle
HEALTHCHECK --interval=1m --start-period=5m \
   CMD "$ORACLE_BASE/$CHECK_DB_FILE" >/dev/null || exit 1
