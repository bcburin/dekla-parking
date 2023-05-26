import axios from "axios";
import store from "src/store/store";

export const baseUrl = "http://127.0.0.1:8000/v1";

const api = axios.create();

api.interceptors.request.use((config) => {
  const state = store.getState();
  const token = state.auth.token;
  config.headers.Authorization = `Bearer ${token}`;
  return config;
});

export default api;
