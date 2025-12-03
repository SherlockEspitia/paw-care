import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api/v1'

export const apiClient = axios.create({
    baseURL: API_BASE_URL,
    headers:{'Content-Type': 'application/json'}
})

apiClient.interceptors.request.use(
    (config)=>{
        /*const token = localStorage.getItem('authToken')
        if (token) config.headers.Authorization = `Bearer ${token}`*/
        console.log(`APPET REQUEST ${config.method?.toUppercase()} ${config.url}`, config.data || ' No se encuentra el Interceptor')
        return config
    },
    (error)=>{
        console.error('APPET REQUEST ERROR', error)
        return Promise.reject(error)
    }
)

apiClient.interceptors.response.use(
    function (response){
        console.log(`APPET RESPONSE ${response.status} ${response.config.url}`, response.data)
        return response
    },
    function(error){
        if(error.response && error.response.status === 401){
            window.location.href = '/login' // Usar React Router
        }
        console.error('APPET RESPONSE ERROR', {
            status: error.response?.status,
            message: error.response?.data?.message || error.message,
            url: error.config?.url
        });
        return Promise.reject(error)
    }
)

export default apiClient
