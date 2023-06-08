import BookmarksRoundedIcon from "@mui/icons-material/BookmarksRounded";
import ChartBarIcon from "@heroicons/react/24/solid/ChartBarIcon";
import CogIcon from "@heroicons/react/24/solid/CogIcon";
import DirectionsCarFilledRoundedIcon from "@mui/icons-material/DirectionsCarFilledRounded";
import LabelIcon from "@mui/icons-material/Label";
import LocalOfferRoundedIcon from "@mui/icons-material/LocalOfferRounded";
import LockClosedIcon from "@heroicons/react/24/solid/LockClosedIcon";
import PublicRoundedIcon from "@mui/icons-material/PublicRounded";
import SecurityRoundedIcon from "@mui/icons-material/SecurityRounded";
import { SvgIcon } from "@mui/material";
import UserIcon from "@heroicons/react/24/solid/UserIcon";
import UserPlusIcon from "@heroicons/react/24/solid/UserPlusIcon";
import UsersIcon from "@heroicons/react/24/solid/UsersIcon";
import VpnLockRoundedIcon from "@mui/icons-material/VpnLockRounded";
import XCircleIcon from "@heroicons/react/24/solid/XCircleIcon";

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
    title: "Labels",
    path: "/labels",
    icon: (
      <SvgIcon fontSize="small">
        <LabelIcon />
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
    showOnlyToAdmins: false,
  },
  {
    title: "Labelings",
    path: "/labelings",
    icon: (
      <SvgIcon fontSize="small">
        <LocalOfferRoundedIcon />
      </SvgIcon>
    ),
    showInSideNav: true,
    showOnlyToAdmins: true,
  },
  {
    title: "Permissions",
    path: "/ep_permission",
    icon: (
      <SvgIcon fontSize="small">
        <SecurityRoundedIcon />
      </SvgIcon>
    ),
    showInSideNav: true,
    showOnlyToAdmins: true,
  },
  {
    title: "Public Policies",
    path: "/public_policy",
    icon: (
      <SvgIcon fontSize="small">
        <PublicRoundedIcon />
      </SvgIcon>
    ),
    showInSideNav: true,
    showOnlyToAdmins: true,
  },
  {
    title: "Exclusive Policies",
    path: "/exclusive_policy",
    icon: (
      <SvgIcon fontSize="small">
        <VpnLockRoundedIcon />
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
