def build_model():
    # Define the machine learning model architecture
    model = Sequential()
    model.add(Dense(128, input_dim=X_train.shape[1], activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    # Compile the model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    return model

def train_model(model, X_train, y_train, X_val, y_val, epochs=10, batch_size=32):
    # Train the model
    history = model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=epochs, batch_size=batch_size)

    # Evaluate the model
    _, accuracy = model.evaluate(X_train, y_train)
    print('Training accuracy: {:.2f}%'.format(accuracy * 100))
    _, accuracy = model.evaluate(X_val, y_val)
    print('Validation accuracy: {:.2f}%'.format(accuracy * 100))

    return history