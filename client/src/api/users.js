import api, { baseUrl, baseUsersApi } from "src/api/api";

export const baseUserUrl = `${baseUrl}/users`;

export const getUsers = async (skip = 0, limit = 100) => {
  const response = await api.get(`${baseUserUrl}/?skip=${skip}&limit=${limit}`);
  const users = response.data;
  return users;
};

export const deleteUser = async (userId) => {
  const response = await api.delete(`${baseUserUrl}/${userId}`);
  const deletedUser = response.data;
  return deletedUser;
};

export const deleteManyUsers = async (userIds) => {
  const response = await api.delete(`${baseUserUrl}/`, { data: userIds });
  const deletedUsers = response.data;
  return deletedUsers;
};

export const createUser = async (user) => {
  const response = await api.post(`${baseUserUrl}/`, {
    username: user.email,
    email: user.email,
    first_name: user.firstName,
    last_name: user.lastName,
    is_admin: false,
    password: user.password,
  });
  const createdUser = response.data;
  return createdUser;
};

export const updateUser = async (userId, user) => {
  const userUpdates = {
    username: user?.email || undefined,
    email: user?.email || undefined,
    first_name: user?.firstName || undefined,
    last_name: user?.lastName || undefined,
    is_admin: false,
    password: user?.password || undefined,
  };

  const response = await api.put(`${baseUserUrl}/${userId}`, userUpdates);
  const updatedUser = response.data;
  return updatedUser;
};

export const toggleAdmin = async (userId) => {
  const response = await api.put(`${baseUserUrl}/${userId}/toggle-admin`);
  const updatedUser = response.data;
  return updatedUser;
};

export const getUserMe = async (userId) => {
  const response = await api.get(`${baseUserUrl}/me`);
  const userMe = response.data;
  return userMe;
};
