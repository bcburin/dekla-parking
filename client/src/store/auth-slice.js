import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  isAuthenticated: false,
  token: null,
  loggedUser: null,
};

const authSlice = createSlice({
  name: "auth",
  initialState,
  reducers: {
    initialize: (state, action) => {
      const token = action.payload;
      const user = action.payload;
      if (token && user) {
        state.isAuthenticated = true;
        state.token = token;
        state.loggedUser = user;
      } else {
        state.isAuthenticated = false;
      }
    },
    signIn: (state, action) => {
      state.isAuthenticated = true;
      state.token = action.payload.token;
      state.loggedUser = action.payload.user;
    },
    signOut: (state) => {
      state.isAuthenticated = false;
      state.token = null;
      state.loggedUser =null;
    },
  },
});

const { reducer, actions } = authSlice;

export const { initialize, signIn, signOut } = actions;

export default reducer;
