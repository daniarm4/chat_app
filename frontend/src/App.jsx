import { BrowserRouter, Routes, Route } from 'react-router-dom';
import React from 'react';
import { useSelector } from 'react-redux';
import { defaultRoutes, protectedRoutes } from './routes';
import Loading from './components/loading/Loading';
import { useCheckAuthQuery } from './store/api/userApi';


const App = () => {
    const { isLoading } = useCheckAuthQuery();
    const { isAuth } = useSelector(state => state.user)
    if (isLoading) {
        return <Loading />;
    }
    return (
        <BrowserRouter>
            <Routes>
                {isAuth 
                ?
                    protectedRoutes.map(route => {
                        return <Route path={route.path} element={route.element}/>
                    })
                :
                    null
                }
                {defaultRoutes.map(route => {
                    return <Route path={route.path} element={route.element} />
                })}
            </Routes>
        </BrowserRouter>
    )
}

export default App;
