from keras.layers.convolutional import Conv2D, MaxPooling2D,AveragePooling2D
from keras.optimizers import adam_v2
from keras.models import Sequential
from keras.layers import Dense, Flatten, GlobalAveragePooling2D, BatchNormalization,Dropout

class Optonet:
    def model(self,img_rows, img_cols, num_channels):
        model = Sequential()
        model.add(
        Conv2D(filters=32, kernel_size=(3, 3), activation='relu', input_shape=(img_rows, img_cols, num_channels)))
        model.add(MaxPooling2D())
        model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
        model.add(MaxPooling2D())
        model.add(Conv2D(filters=128, kernel_size=(3, 3), activation='relu'))
        model.add(MaxPooling2D())
        model.add(Flatten())
        model.add(Dense(units=256, activation='relu'))
        model.add(Dropout(0.2))
        model.add(Dense(units=128, activation='relu'))
        model.add(Dense(units=2, activation='sigmoid'))
        model.compile(optimizer=adam_v2(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])
        model.summary()
        return model