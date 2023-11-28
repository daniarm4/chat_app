import { createSlice } from "@reduxjs/toolkit"
import { checkAuth } from "../api/userApi";

const initialAuthState = {
    username: null,
    userId: null,
    isAuth: false
}

export const userSlice = createSlice({
    name: 'user',
    initialState: initialAuthState,
    reducers: {
        userLogout(state) {
            localStorage.removeItem('accessToken');
            localStorage.removeItem('refreshToken');
            state.username = '';
            state.userId = null;
            state.isAuth = false;
        }
    },
    extraReducers: builder => {
        builder.addMatcher(checkAuth.matchFulfilled, (state, action) => {
            state.isAuth = true;
            state.userId = action.payload.id;
            state.username = action.payload.username;
        })
    }
})

const { actions, reducer } = userSlice;

export const { userLogout, userLogin } = actions;

export default reducer;
