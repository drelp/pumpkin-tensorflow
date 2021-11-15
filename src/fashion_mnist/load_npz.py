import numpy as np

# 假设数据保存在'./datasets/'文件夹下
try:
    data = np.load('./datasets/mnist.npz')
    x_train, y_train, x_test, y_test = data['x_train'], data['y_train'], data['x_test'], data['y_test']

    # 可以将其中一条数据保存成txt文件，查看一下，会对这组数据有个直观的感受
    # np.savetxt('test.txt',x_train[0],fmt='%3d',newline='\n\n')

    # 将数据归一化
    x_train, x_test = x_train / 255.0, x_test / 255.0
except Exception as e:
    print('%s' % e)