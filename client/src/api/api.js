import axios from "axios";
import store from "src/store/store";

export const baseRootUrl = "http://127.0.0.1:8000/v1";

const api = axios.create();

api.interceptors.request.use((config) => {
  const state = store.getState();
  const token = state.auth.token;
  config.headers.Authorization = `Bearer ${token}`;
  return config;
});

export const createBaseAPI = (entityName) => {
  const baseUrl = `${baseRootUrl}/${entityName}`;

  return {
    baseUrl,
    getEntities: async (skip = 0, limit = 500) => {
      const response = await api.get(`${baseUrl}/?skip=${skip}&limit=${limit}`);
      return response.data;
    },
    deleteEntity: async (entityId) => {
      const response = await api.delete(`${baseUrl}/${entityId}`);
      return response.data;
    },
    deleteManyEntities: async (entityIds) => {
      const response = await api.delete(`${baseUrl}/`, { data: entityIds });
      return response.data;
    },
    createEntity: async (entity) => {
      const response = await api.post(`${baseUrl}/`, entity);
      return response.data;
    },
    updateEntity: async (entityId, entityUpdates) => {
      const truthyUpdates = Object.fromEntries(
        Object.entries(entityUpdates).filter(([key, value]) => value)
      );
      const response = await api.put(`${baseUrl}/${entityId}`, truthyUpdates);
      return response.data;
    },
  };
};

export default api;
