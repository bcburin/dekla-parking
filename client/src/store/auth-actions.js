import axios from "axios";
import { signIn } from "./auth-slice";

const baseUrl = "http://127.0.0.1:8000/v1";

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

      dispatch(signIn(token));
    } catch (error) {
      throw new Error("Invalid email or password");
    }
  };
};

export const register = async (user) => {
  try {
    const response = await axios.post(`${baseUrl}/users`, {
      username: user.email.replace(/@.*/, ""),
      email: user.email,
      first_name: user.firstName,
      last_name: user.lastName,
      is_admin: false,
      password: user.password,
    });

    console.log(response);
  } catch (e) {
    throw new Error("Unable to create user");
  }
};
