import axios from "axios";
import { signIn } from "./auth-slice";

export const baseUrl = "http://127.0.0.1:8000/v1";

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
        `${baseUrl}/users/login`,
        formData,
        config
      );

      const token = response.data.access_token;

      localStorage.setItem("accessToken", token);

      dispatch(signIn({ token }));
    } catch (error) {
      throw new Error("Invalid email or password");
    }
  };
};
