##Practice1
# if __name__ == "__main__":
#     print("Hello world")

##Practice2
# A = input("Aさんの年齢を入力して下さい > ")
# B = input("Bさんの年齢を入力して下さい > ")
# res = int(A) - int(B)
# print(res)

##Practice3
# res = 0
# for i in range(100):res = res + i +1
# print(res)    #5050

##Practice4
# res = 0
# for i in range(100):
# 	res = res + i + 1
# 	print(i+1)
# print(res)

##Practice5
# res = 0
# for i in range(100):
#     if i%2==0:
#         res = res+i+1
#     else:
#         res = res-i-1
# print(res)  #-50

##Practice6
# import numpy
# a = numpy.array([1,2,3,4,5])
# res = numpy.average(a)
# print(res)  #3.0

##Practice7
# import datetime
# weekdays = ("月","火","水","木","金","土","日")
# t = datetime.date.today()
# w = t.weekday()
# print(weekdays[w])  #今日の曜日

##Practice8
# key_in = []
# for i in range(4):
#     data = input(str(i) + "つめの数字を入れて下さい >")
#     data_int = int(data)
#     key_in.append(data_int)
# print(key_in)   #入力した数字
# print(sum(key_in))  #全ての合計

##Practice9
# import random
# computer = random.randint(0,2)
# user = int(input("0..グー, 1..チョキ, 2..パー　いずれかを入力してください > "))
# if user - computer == 0:
#     res = "あいこ"
# elif user - computer == 2 or user - computer == -1:
#     res = "あなたの勝ち"
# else:
#     res = "コンピューターの勝ち"
#
# rps_describe = ("グー", "チョキ","パー")
#
# print("コンピューター:"+rps_describe[computer])
# print("あなた:"+rps_describe[user])
# print(res)

##Practice10
# import random
# computer = random.randint(0,2)
# user = int(input("0..グー, 1..チョキ, 2..パー　いずれかを入力してください > "))
# matrix = (("あいこ","コンピューターの勝ち","あなたの勝ち"),
#           ("あなたの勝ち","あいこ","コンピューターの勝ち"),
#           ("コンピューターの勝ち", "あなたの勝ち","あいこ"))
# rps_describe = ("グー", "チョキ","パー")
# print("コンピューター:" + rps_describe[computer])
# print("あなた:" + rps_describe[user])
# print(matrix[computer][user])

##Practice11
# a =[]
# for i in range(10):
#     a.append(i)
# print(a)    #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# b = [i for i in range(10)]
# print(b)    #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# c = [i for i in range(10) if i % 2 == 0]
# print(c)    #[0, 2, 4, 6, 8]

##Practice12
# d = {'yamada':30, 'suzuki':40}
# print(d['yamada'])  #30
#
# t = [{'EmployeeNo':'E001', 'Name':'Yamada','Age':40},
#      {'EmployeeNo': 'E002', 'Name': 'Kobayashi', 'Age': 55},
#      {'EmployeeNo': 'E003', 'Name': 'Tanaka', 'Age': 30}]
# res = [x for x in t if x['EmployeeNo']=='E002']
# print(res)  #[{'Name': 'Kobayashi', 'Age': 55, 'EmployeeNo': 'E002'}]
#
# res = sorted(t, key=lambda x:x['Age'])
# print(res)  #[{'EmployeeNo': 'E003', 'Name': 'Tanaka', 'Age': 30}, {'EmployeeNo': 'E001', 'Name': 'Yamada', 'Age': 40}, {'EmployeeNo': 'E002', 'Name': 'Kobayashi', 'Age': 55}]
#
# res = sorted(t, key=lambda x:x['Age'],reverse=True)
# print(res)  #[{'Age': 55, 'EmployeeNo': 'E002', 'Name': 'Kobayashi'}, {'Age': 40, 'EmployeeNo': 'E001', 'Name': 'Yamada'}, {'Age': 30, 'EmployeeNo': 'E003', 'Name': 'Tanaka'}]

##Practice13
# import numpy
# a = numpy.array([1,2,3,4,5])
# print(a)    #[1 2 3 4 5]
# print(a*2)  #[ 2  4  6  8 10]
# print(numpy.sin(a)) #[ 0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427]
#
# b = numpy.array([
#      [1,2,3],
#      [4,5,6],
#      [7,8,9],
#      [10,11,12]
# ])
# v = numpy.array([10,20,30])
# print(numpy.dot(b,v))   #[140 320 500 680]

##Practice14
# import numpy
# import matplotlib.pyplot
# x = numpy.arange(-3,3,0.01)
# y = numpy.sin(x)
# matplotlib.pyplot.plot(x,y)
# matplotlib.pyplot.show()

##Practice15
# import numpy
# import matplotlib.pyplot
# import matplotlib.animation

#グラフのエリアを作る
# fig = matplotlib.pyplot.figure()
# matplotlib.pyplot.xlim([-1,1])    #x軸の幅を決める
# matplotlib.pyplot.ylim([-1,1])    #y軸の幅を決める
# matplotlib.pyplot.grid()          #Gridを描く

#原点から(0,-1)のベクトルを作る
# t = numpy.array([0,1])
# matplotlib.pyplot.plot([0,t[0]],[0,t[1]],'k-')    #(0,0)から(0,1）まで黒で線を引く optionの種類は　https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot
# #matplotlib.pyplot.show()

# #アニメーションを作る
# t1 = numpy.array([0,1])
# t2 = numpy.array([0,-1])
#
# ims = []
# im = matplotlib.pyplot.plot([0,t1[0]],[0,t1[1]],'k-')
# ims.append(im)
# im = matplotlib.pyplot.plot([0,t2[0]],[0,t2[1]],'k-')
# ims.append(im)
#
# ani = matplotlib.animation.ArtistAnimation(fig,ims,interval=1000)   # https://matplotlib.org/api/_as_gen/matplotlib.animation.ArtistAnimation.html#matplotlib.animation.ArtistAnimation
#
# matplotlib.pyplot.draw()
# matplotlib.pyplot.show()

# #回転行列を使って原点を中心に回転させる
# import numpy
# import matplotlib.pyplot
# import matplotlib.animation
#
# fig = matplotlib.pyplot.figure()
# matplotlib.pyplot.xlim([-1,1])
# matplotlib.pyplot.ylim([-1,1])
# matplotlib.pyplot.grid()
#
# t = numpy.array([0,1])
# ims = []
# for r in numpy.linspace(2*numpy.pi,0, 360):
#      r_array = numpy.array([
#           [numpy.cos(r), -1 * numpy.sin(r)],
#           [numpy.sin(r), numpy.cos(r)]
#      ])
#      t_r = numpy.dot(r_array, t)
#
#      im = matplotlib.pyplot.plot([0,t_r[0]],[0,t_r[1]], 'k-')
#      ims.append(im)
#      print(t_r)
#
# ani = matplotlib.animation.ArtistAnimation(fig, ims, interval=50)
# matplotlib.pyplot.draw()
# matplotlib.pyplot.show()

##Practice16
#16-1
import sklearn.datasets
iris = sklearn.datasets.load_iris()
# print(iris)
#print(iris.keys())  #dict_keys(['DESCR', 'feature_names', 'target_names', 'data', 'target'])

#16-2
import sklearn.svm
clf = sklearn.svm.SVC()

data = iris['data']
target = iris['target']

clf.fit(data,target)

#16-3
import random
row = random.randint(0,len(data)-1)
p_data = data[row].reshape(1,len(data[row]))
p_target = clf.predict(p_data)

print(p_data)
print("予測:" + str(p_target[0]))
print("正解:"+str(target[row]))