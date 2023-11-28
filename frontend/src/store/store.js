import { combineReducers, configureStore } from '@reduxjs/toolkit';
import userReducer from './reducers/userSlice';
import notificationReducer from './reducers/notificationSlice';
import chatReducer from './reducers/chatSlice';
import { api } from './api/base';

const reducers = combineReducers({
    user: userReducer,
    notifications: notificationReducer,
    chat: chatReducer,
    [api.reducerPath]: api.reducer
})

const store = configureStore({
    reducer: reducers,
    middleware: (getDefaultMiddleware) => 
        getDefaultMiddleware().concat(api.middleware)
})

export default store;
