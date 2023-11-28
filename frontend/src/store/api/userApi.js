import { api } from "./base";

const userApi = api.injectEndpoints({
    endpoints: (builder) => ({
        checkAuth: builder.query({
            query: () => '/users/me'
        }),
        login: builder.mutation({
            query: (data) => ({
                url: '/users/login',
                method: 'POST',
                body: data
            }) 
        }),
        register: builder.mutation({
            query: (data) => ({
                url: '/users/register',
                method: 'POST',
                body: data
            })
        }),
        getUser: builder.query({
            query: username => `/users/${username}`
        })
    })
})

export const { useCheckAuthQuery, useLoginMutation, useRegisterMutation, useGetUserQuery } = userApi;

export const {endpoints: { checkAuth } } = userApi;
