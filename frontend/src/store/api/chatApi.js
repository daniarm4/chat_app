import { api } from './base'

export const chatApi = api.injectEndpoints({
    endpoints: (builder) => ({
        getMessages: builder.query({
            query: chatId => `/chats/${chatId}/messages`, 
            providesTags: ((result, error, id) => [{
                type: 'Chats',
                id: id
            }]),
        }),
        getChatsByUserId: builder.query({
            query: () => '/chats/by_user',
        }),
        createChat: builder.mutation({
            query: chatData => ({
                url: '/chats',
                method: 'POST',
                body: chatData
            })
        })
    })
})

export const { useGetMessagesQuery, useGetChatsByUserIdQuery, useCreateChatMutation } = chatApi;
