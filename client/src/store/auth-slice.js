import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  isAuthenticated: false,
  token: null,
};

const authSlice = createSlice({
  name: "auth",
  initialState,
  reducers: {
    initialize: (state, action) => {
      const token = action.payload;
      if (token) {
        state.isAuthenticated = true;
        state.token = token;
      } else {
        state.isAuthenticated = false;
      }
    },
    signIn: (state, action) => {
      state.isAuthenticated = true;
      state.token = action.payload;
    },
    signOut: (state) => {
      state.isAuthenticated = false;
      state.token = null;
    },
  },
});

const { reducer, actions } = authSlice;

export const { initialize, signIn, signOut } = actions;

export default reducer;
