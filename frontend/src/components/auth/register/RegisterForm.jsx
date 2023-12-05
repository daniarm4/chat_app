import React from 'react';
import { useFormik } from 'formik';
import * as yup from 'yup';
import { useRegisterMutation } from '../../../store/api/userApi';
import { useNavigate } from 'react-router-dom';

const RegisterForm = () => {
    const navigate = useNavigate();
    const [registerUser, {isLoading, isError, isSuccess, data}] = useRegisterMutation();

    const validationSchema = yup.object({
        username: yup.string()
            .min(3, 'Min character length 3')
            .max(50, 'Max character length 50')
            .required('Username is required'),
        password: yup.string()
            .min(8, 'Min password length 8')
            .max(16, 'Max password length 16')
            .required('Password is required'),
        rePassword: yup.string()
            .oneOf([yup.ref('password')], 'Password must match')
            .required('Password is required')
    })

    const formik = useFormik({
        initialValues: {
            'username': '',
            'password': '',
            'rePassword': ''
        },
        validationSchema: validationSchema,
        onSubmit: (values) => {
            const registerData = {
                username: values.username,
                password: values.password, 
                re_password: values.rePassword
            };
            registerUser(registerData);
        }
    });

    if (isSuccess) {
        navigate('/login');
    }

    if (isLoading) {
        console.log('loading');
    }

    if (isError) {
        console.log('error');
        console.log(data);
    }

    const fields = [
        {id: 'username', type: 'text', placeholder: 'Username'},
        {id: 'password', type: 'password', placeholder: 'Password'},
        {id: 'rePassword', type: 'password', placeholder: 'Repeat password'}
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
            <button type='submit'>Sign up</button>
        </form>
    )
}

export default RegisterForm;
