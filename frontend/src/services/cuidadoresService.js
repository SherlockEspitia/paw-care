import apiClient from "./apiClient";

const BASE_PATH = '/cuidadores'

export const listCuidadores = async(params = {})=>{
    const res = await apiClient.get(BASE_PATH, {params})
    // normalizar
    return res.data
}

export const getCuidador = async (id)=>{
    const res = await apiClient.get(`${BASE_PATH}/${id}`);
    return res.data
}

export const createCuidador = async (cargaCuidador)=>{
    const res = await apiClient.post(BASE_PATH, cargaCuidador)
    return res.data
}

export const updateCuidador = async (id, cargaCuidador)=>{
    const res = await apiClient.put(`${BASE_PATH}/${id}`, cargaCuidador)
    return res.data
}

export const deleteCuidador = async(id) => {
    const res = await apiClient.delete(`${BASE_PATH}/${id}`)
    return res.data
}

export default{ listCuidadores, getCuidador, createCuidador, updateCuidador, deleteCuidador}
/*export const cuidadoresService = {
    //getAll:()=>apiClient.get(`/cuidadores`),
    getById:(id)=>apiClient.get(`${BASE_PATH}/${id}`),
    create:(cuidadordata)=>apiClient.post(`/cuidadores/`,cuidadordata),
    update:(id)=>apiClient.put(`/cuidadores/${id}`),
    delete:(id)=>apiClient.delete(`/cuidadores/${id}`)
}*/