import { createSlice } from '@reduxjs/toolkit';

const initialNotificationState = {
    notificationList: []
}

export const notificationSlice = createSlice({
    name: 'notification',
    initialState: initialNotificationState,
    reducers: {},
})

const { reducer } = notificationSlice;

export default reducer;
