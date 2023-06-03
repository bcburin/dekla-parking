import BookmarksRoundedIcon from "@mui/icons-material/BookmarksRounded";
import CogIcon from "@heroicons/react/24/solid/CogIcon";
import DirectionsCarFilledRoundedIcon from "@mui/icons-material/DirectionsCarFilledRounded";
import LockClosedIcon from "@heroicons/react/24/solid/LockClosedIcon";
import { SvgIcon } from "@mui/material";
import UserIcon from "@heroicons/react/24/solid/UserIcon";
import UserPlusIcon from "@heroicons/react/24/solid/UserPlusIcon";
import UsersIcon from "@heroicons/react/24/solid/UsersIcon";
import XCircleIcon from "@heroicons/react/24/solid/XCircleIcon";
import ChartBarIcon from "@heroicons/react/24/solid/ChartBarIcon";

export const items = [
  {
    title: "Overview",
    path: "/",
    icon: (
      <SvgIcon fontSize="small">
        <ChartBarIcon />
      </SvgIcon>
    ),
    showInSideNav: false,
    showOnlyToAdmins: false,
  },
  {
    title: "Parking Lots",
    path: "/sectors",
    icon: (
      <SvgIcon fontSize="small">
        <DirectionsCarFilledRoundedIcon />
      </SvgIcon>
    ),
    showInSideNav: true,
    showOnlyToAdmins: false,
  },
  {
    title: "Users",
    path: "/users",
    icon: (
      <SvgIcon fontSize="small">
        <UsersIcon />
      </SvgIcon>
    ),
    showInSideNav: true,
    showOnlyToAdmins: true,
  },
  {
    title: "Bookings",
    path: "/bookings",
    icon: (
      <SvgIcon fontSize="small">
        <BookmarksRoundedIcon />
      </SvgIcon>
    ),
    showInSideNav: true,
    showOnlyToAdmins: true,
  },
  {
    title: "Account",
    path: "/account",
    icon: (
      <SvgIcon fontSize="small">
        <UserIcon />
      </SvgIcon>
    ),
    showInSideNav: true,
    showOnlyToAdmins: false,
  },
  {
    title: "Settings",
    path: "/settings",
    icon: (
      <SvgIcon fontSize="small">
        <CogIcon />
      </SvgIcon>
    ),
    showInSideNav: true,
    showOnlyToAdmins: false,
  },
  {
    title: "Login",
    path: "/auth/login",
    icon: (
      <SvgIcon fontSize="small">
        <LockClosedIcon />
      </SvgIcon>
    ),
    showInSideNav: false,
    showOnlyToAdmins: false,
  },
  {
    title: "Register",
    path: "/auth/register",
    icon: (
      <SvgIcon fontSize="small">
        <UserPlusIcon />
      </SvgIcon>
    ),
    showInSideNav: false,
    showOnlyToAdmins: false,
  },
  {
    title: "Error",
    path: "/404",
    icon: (
      <SvgIcon fontSize="small">
        <XCircleIcon />
      </SvgIcon>
    ),
    showInSideNav: false,
    showOnlyToAdmins: false,
  },
];
