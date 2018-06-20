import os,pickle

from config import opration_file

f = opration_file.Opration_file()

class Resource:
    def get_resource(self,name):
        if not os.path.exists('../db/%s.pkl'%name):
            print('请先创建%s列表'%name)
        else:
            resource_pkl = f.read_file('../db/%s.pkl'%name, 'rb')
            resource_list = pickle.load(resource_pkl)
            print(resource_list)
            return resource_list

    def set_resource(self,resource_name,name):
        if not os.path.exists('../db/%s.pkl'%name):
            resource_pkl = f.write_file('../db/%s.pkl'%name, 'wb')
            resource_list = []
            for resource in resource_name:
                resource_list.append(resource)
                print('成功将%s添加到%s列表'%(resource,name))
            pickle.dump(resource_list,resource_pkl)
        else:
            resource_list = self.get_resource(name)
            for resource in resource_name:
                resource_list.append(resource)
                print('成功将%s添加到%s列表' % (resource, name))
            resource_pkl = f.write_file('../db/%s.pkl'%name, 'wb')
            pickle.dump(resource_list,resource_pkl)

    def del_resource(self,resource_name,name):
        if not os.path.exists('../db/%s.pkl'%name):
            print('请先创建%s列表'%name)
        else:
            resource_list = self.get_resource(name)
            for resource in resource_name:
                if resource in resource_list:
                    resource_list.remove(resource)
                    resource_pkl = f.write_file('../db/%s.pkl'%name, 'wb')
                    pickle.dump(resource_list,resource_pkl)
                    print('%s已被成功删除'%name)
                else:
                    print('%s不存在，无法删除'%name)