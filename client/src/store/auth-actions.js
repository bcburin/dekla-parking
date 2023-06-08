import { signIn, signOut } from "./auth-slice";

import axios from "axios";
import { baseRootUrl } from "src/api/api";

export const login = (email, password) => {
  return async (dispatch) => {
    try {
      const formData = new FormData();
      formData.append("grant_type", "password");
      formData.append("username", email);
      formData.append("password", password);

      const config = {
        headers: {
          "content-type": "multipart/form-data",
        },
      };

      const response = await axios.post(
        `${baseRootUrl}/users/login`,
        formData,
        config
      );

      const token = response.data.access_token;

      const userResponse = await axios.get(`${baseRootUrl}/users/me`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      const user = userResponse.data;

      localStorage.setItem("accessToken", token);

      dispatch(signIn({ token, user }));
    } catch (error) {
      throw new Error("Invalid email or password");
    }
  };
};

export const logout = () => {
  return async (dispatch) => {
    localStorage.clear();
    dispatch(signOut());
  };
};
