import React from 'react';
import { useFormik } from 'formik';
import * as yup from 'yup';
import { useNavigate } from 'react-router-dom';
import { useLoginMutation } from '../../store/api/userApi';

const LoginForm = () => {
    const navigate = useNavigate();
    const [userLogin, {data, isLoading, isError, isSuccess}] = useLoginMutation();

    const validationSchema = yup.object({
        username: yup.string()
            .min(3, 'Min 3 characters')
            .max(50, 'Must be 50 characters or less')
            .required('Username is required'),
        password: yup.string()
            .min(8, 'Min 8 characters')
            .max(16, 'Must be 16 characters or less')
            .required('Password is required')
    })

    const formik = useFormik({
        initialValues: {
            username: '',
            password: ''
        },
        validationSchema: validationSchema,
        onSubmit: (values) => {
            console.log('submit');
            userLogin({
                username: values.username, password: values.password
            })
        }
    });

    if (isLoading) {
        console.log('loading');
    }

    if (isSuccess) {
        localStorage.setItem('accessToken', data.access_token);
        localStorage.setItem('refreshToken', data.refresh_token);
        navigate('/chats');
    }
    
    if (isError) {
        console.log('error');
        console.log(data);
    }

    const fields = [
        {id: 'username', type: 'text', placeholder: 'Username'},
        {id: 'password', type: 'password', placeholder: 'Password'},
    ]

    return (
        
        <form onSubmit={formik.handleSubmit}>
            {fields.map(field => {
                return (
                    <>
                        <input 
                            id={field.id}
                            type={field.type} 
                            placeholder={field.placeholder} 
                            {...formik.getFieldProps(field.id)}
                            >
                        </input>
                        {formik.touched[field.id] && formik.errors[field.id] ? 
                        <div className='field-errors'>{formik.errors[field.id]}</div>
                        : null}
                    </>
                )
            })}
            <button type='submit'>Login</button>
        </form>
    )
}

export default LoginForm;
