import authReducer from "./auth-slice";
import { configureStore } from "@reduxjs/toolkit";
import lotUIReducer from "./lot-ui-slice";

const store = configureStore({
  reducer: {
    auth: authReducer,
    lotUI: lotUIReducer,
  },
  devTools: process.env.NODE_ENV !== "production",
});

export default store;
