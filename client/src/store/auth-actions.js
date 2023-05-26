import axios from "axios";
import { baseRootUrl } from "src/api/api";
import { signIn } from "./auth-slice";

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

      localStorage.setItem("accessToken", token);

      dispatch(signIn({ token }));
    } catch (error) {
      throw new Error("Invalid email or password");
    }
  };
};
