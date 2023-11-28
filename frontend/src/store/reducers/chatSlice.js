import { createSlice } from "@reduxjs/toolkit";

const initialChatState = {
    chatId: null,
    chatName: null,
}

export const ChatSlice = createSlice({
    name: 'chat',
    initialState: initialChatState,
    reducers: {
        setChat(state, action) {
            state.chatId = action.payload.chatId;
            state.chatName = action.payload.chatName;
        }
    }
})

const { reducer, actions } = ChatSlice;

export const { setChat } = actions;

export default reducer;
