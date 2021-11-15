import read

train_image_filename = 'data/train-images-idx3-ubyte.gz'
train_label_filename = 'data/train-labels-idx1-ubyte.gz'
test_image_filename = 'data/t10k-images-idx3-ubyte.gz'
test_label_filename = 'data/t10k-labels-idx1-ubyte.gz'

x_train = read.get_images(train_image_filename).reshape(-1, 28, 28) / 255.
y_train = read.get_labels(train_label_filename)
x_test = read.get_images(test_image_filename).reshape(-1, 28, 28) / 255.
y_test = read.get_labels(test_label_filename)