import os,pickle

from config import opration_file

f = opration_file.Opration_file()

class Score:
    def add_score(self,group_list):
        if os.path.exists('../db/student.pkl'):
            if os.path.exists('../db/group.pkl'):
                group_info = f.read_file('../db/group.pkl', 'rb')

                while True:
                    for i, v in enumerate(group_list):
                        print(str(i + 1) + '、' + v)

                    group_num = input('您要为哪个班级打分？请输入班级序号：')
                    if group_num.isdigit():
                        group_num = int(group_num)
                        if group_num in list(range(len(group_list) + 1))[1:]:
                            group = group_list[(group_num - 1)]
                            if len(group_info[group]['student']) > 0:
                                print('%s班级的学员如下：' % group)
                                print(','.join(group_info[group_list[(group_num - 1)]]['student']))

                                while True:
                                    student_name = input('您要为哪个学员打分？请输入学员姓名：')

                                    if student_name not in group_info[group]['student']:
                                        print('您输的同学不存在，请重新输入')
                                        continue

                                    student_score = input('请输入分数：')

                                    if not os.path.exists('../db/score.pkl'):
                                        score_pkl = f.write_file('../db/score.pkl', 'wb')
                                        score_info = {}
                                        score_info[group] = {'course': group_info[group]['course'], 'score':{student_name:{'score': student_score}}}
                                        print('录入成功，%s班的同学，在班级开设的%s课程中，获得%s分' % (
                                        group, group_info[group]['course'], student_score))

                                        pickle.dump(score_info, score_pkl)
                                        return
                                    else:
                                        score_info = f.read_file('../db/score.pkl','rb')
                                        if student_name in score_info[group]['score'].keys():
                                            print('您已经为该学员打过分了')
                                            return
                                        else:
                                            score_info[group]['score'][student_name] = {'score': student_score}
                                            print('录入成功，%s班的同学，在班级开设的%s课程中，获得%s分' % (
                                                group, group_info[group]['course'], student_score))
                                            score_pkl = f.write_file('../db/score.pkl', 'wb')
                                            pickle.dump(score_info, score_pkl)
                                            return

                            else:
                                print('您管理的班级，还没有学生选择，等待已认证的同学加入吧')
                                return
                        else:
                            print('序号输入错误，请重新输入')
                            continue
                    else:
                        print('序号输入错误，请重新输入')
                        continue
            else:
                print('还没有开班哦，请等待管理员创建班级')
                return
        else:
            print('还没有认证的同学，请您先等待学生的加入吧')
            return

    def edit_score(self,group_list):
        if os.path.exists('../db/score.pkl'):
            if os.path.exists('../db/student.pkl'):
                if os.path.exists('../db/group.pkl'):

                    group_info = f.read_file('../db/group.pkl', 'rb')

                    while True:
                        for i, v in enumerate(group_list):
                            print(str(i + 1) + '、' + v)
                        group_num = input('请选择班级，输入班级序号：')

                        if int(group_num) in list(range(len(group_list) + 1)):
                            group = group_list[(int(group_num) - 1)]
                            if len(group_info[group]['student']) > 0:
                                print('%s班级的学员如下：' % group)
                                print(','.join(group_info[group_list[(int(group_num) - 1)]]['student']))

                                while True:
                                    student_name = input('您要为哪个学员打分？请输入学员姓名：')

                                    score_info = f.read_file('../db/score.pkl', 'rb')

                                    if student_name not in score_info[group]['score'].keys():
                                        print('%s学员还没有过成绩，请先为该同学打分'%student_name)
                                        return

                                    if student_name not in group_info[group]['student']:
                                        print('您输的同学不存在，请重新输入')
                                        continue

                                    student_score = input('请输入分数：')

                                    score_info = f.read_file('../db/score.pkl', 'rb')

                                    score_bk = score_info[group]['score'][student_name]['score']
                                    score_info[group]['score'][student_name]['score'] = student_score

                                    print('修改成功，%s班的同学，在班级开设的%s课程中，将原分数%s分修改为%s分' %(group, group_info[group]['course'], score_bk,student_score))

                                    score_pkl = f.write_file('../db/score.pkl', 'wb')
                                    pickle.dump(score_info, score_pkl)
                                    return
                            else:
                                print('您管理的班级，还没有学生选择，等待已认证的同学加入吧')
                                return
                        else:
                            print('序号输入错误，请重新输入')
                            continue
                else:
                    print('还没有开班哦，请等待管理员创建班级')
                    return
            else:
                print('还没有认证的同学，请您先等待学生的加入吧')
                return
        else:
            print('您还没有为学员打过分，请先为学员打分吧')
            return