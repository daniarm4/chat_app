import { fetchBaseQuery } from '@reduxjs/toolkit/query'
import { createApi } from '@reduxjs/toolkit/query/react';

const baseQuery = fetchBaseQuery({
    baseUrl: 'http://127.0.0.1:8000',
    credentials: 'include',
    prepareHeaders: (headers) => {
        const accessToken = localStorage.getItem('accessToken');
        if (accessToken) {
            headers.set('Authorization', `Bearer ${accessToken}`);
        };
        return headers;
    },
})

const baseQueryWithReauth = async (args, api, extraOptions) => {
    let response = await baseQuery(args, api, extraOptions)
    if (response.error && response.error.status === 401) {
        localStorage.removeItem('accessToken');
        console.log(response.error);
        const refreshToken = localStorage.getItem('refreshToken');
        const refreshResult = await baseQuery(
            {url: '/users/refresh', method: 'POST', headers: {Authorization: `Bearer ${refreshToken}`}}, 
            api, extraOptions
        );
        if (refreshResult.data) {
            localStorage.setItem('accessToken', refreshResult.data.access_token);
            response = await baseQuery(args, api, extraOptions)
        } else {
            console.log(refreshResult);
        }
    }
    return response;
}

export const api = createApi({
    reducerPath: 'api',
    baseQuery: baseQueryWithReauth,
    tagTypes: ['Chats', 'Users', 'Notifications'],
    endpoints: () => ({})
})


