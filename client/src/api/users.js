import api, { baseRootUrl, createBaseAPI } from "src/api/api";

const baseUserUrl = `${baseRootUrl}/users`;

const userAPI = {
  ...createBaseAPI("users"),
  toggleAdmin: async (userId) => {
    const response = await api.put(`${baseUserUrl}/${userId}/toggle-admin`);
    return response.data;
  },
  getUserMe: async () => {
    const response = await api.get(`${baseUserUrl}/me`);
    return response.data;
  },
};

export default userAPI;
