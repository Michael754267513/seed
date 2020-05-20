# -*- coding: utf-8 -*-
import MySQLdb

class dbsql(object):

    def __init__(self,host,username,password,db="seed"):
         self.db = MySQLdb.connect(host,username,password,db,charset='utf8')
         self.cursor = self.db.cursor()

    def get_deployment(self, meta):
        try:
            self.cursor.execute('''select deployment from prjhis where env = '%s' ''' %
                                (meta["env"]))
            data = self.cursor.fetchall()
            return True, data
        except Exception as e:
            print(e)
            return False, e

    def get_project(self):
        self.cursor.execute('''select * from prjhis''')
        data = self.cursor.fetchall()
        return data

    def get_svc(self, project):
        try:
            self.cursor.execute(
                '''SELECT pj.prjname,sv.`images`,sv.`service`,sv.`svcname` FROM project pj,services sv WHERE pj.`prjname` = '%s' ''' % (project))
            data = self.cursor.fetchall()
            return True, data
        except Exception as e:
            print(e)
            return False, e

    def check_exist(self,pkg_meta):
        try:
            sql = '''SELECT COUNT(0) from prjhis
                                                    where env='%s' and project='%s' and pkgname='%s' and 
                                                    type='%s' and deployment='%s'
                                                    ''' % (
                    pkg_meta["env"],
                    pkg_meta["project"],
                    pkg_meta["packagename"],
                    pkg_meta["type"],
                    pkg_meta["deployment"]
                )
            print sql
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            check_exist_count = False
            for count in data:
                if int(count[0]) == 0:
                    check_exist_count = True
            return True, check_exist_count
        except Exception as e:
            print(e)
            self.db.rollback()
            return False, e

    def update_deployment(self, meta):
        try:
            for pkg_meta in meta:
                self.cursor.execute('''update prjhis set image ='%s' 
                                    where env='%s' and project='%s' and pkgname='%s' and 
                                    type='%s' and deployment='%s'
                                    ''' % (
                                        pkg_meta["image"],
                                        pkg_meta["env"],
                                        pkg_meta["project"],
                                        pkg_meta["packagename"],
                                        pkg_meta["type"],
                                        pkg_meta["deployment"]
                                        ))
            self.db.commit()
            return True, None
        except Exception as e:
            print(e)
            self.db.rollback()
            return False, e

    def create_deployment(self, meta):
        try:
            for pkg_meta in meta:
                sql = '''insert into prjhis(pkgname,type,image,project,env,owner,ingress,deployment,isingress) 
                                    values '%s','%s','%s','%s','%s','%s','%s','%s','%s')''' %(pkg_meta["packagename"],
                                     pkg_meta["type"],
                                     pkg_meta["image"],
                                     pkg_meta["project"],
                                     pkg_meta["env"],
                                     pkg_meta["owner"],
                                     pkg_meta["ingress_name"],
                                     pkg_meta["deployment"],
                                     pkg_meta["ingress"])
                print(sql)
                self.cursor.execute('''insert into prjhis(pkgname,type,image,project,env,owner,ingress,deployment,isingress) 
                                    values 
                                    ('%s','%s','%s','%s','%s','%s','%s','%s','%s')''' %
                                    (pkg_meta["packagename"],
                                     pkg_meta["type"],
                                     pkg_meta["image"],
                                     pkg_meta["project"],
                                     pkg_meta["env"],
                                     pkg_meta["owner"],
                                     pkg_meta["ingress_name"],
                                     pkg_meta["deployment"],
                                     pkg_meta["ingress"]
                                     ))
            self.db.commit()
            return True, None
        except Exception as e:
            print(e)
            self.db.rollback()
            return False, e

    def delete_deployment(self, meta):
        try:
            for pkg_meta in meta:
                self.cursor.execute('''delete from prjhis
                                                    where env='%s' and project='%s' and pkgname='%s' and 
                                                    type='%s' and deployment='%s'
                                                    ''' % (
                    pkg_meta["env"],
                    pkg_meta["project"],
                    pkg_meta["packagename"],
                    pkg_meta["type"],
                    pkg_meta["deployment"]
                ))
                self.db.commit()
            return True, None
        except Exception as e:
            print(e)
            self.db.rollback()
            return False, e

    def delete_env(self, meta):
        try:
            self.cursor.execute('''delete from prjhis
                                                where env='%s'
                                                ''' % (meta["env"]))
            self.db.commit()
            return True, None
        except Exception as e:
            print(e)
            self.db.rollback()
            return False, e

    def get_env_deployment(self, env='%'):
        try:
            self.cursor.execute(
                '''SELECT pkgname,env FROM prjhis where env like  '%s' '''%env)
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            print(e)
            return False, e

    def close(self):
        self.db.close()





