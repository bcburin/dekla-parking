import { Card, Typography } from "@mui/material";

const ShowUserModal = ({ user }) => {
  return;
  <>
    <Card>
      <Typography variant="h2">
        {user.firstName} {user.lastName}
      </Typography>
      <Typography>{user.email}</Typography>
      <Typography>{user.id}</Typography>
    </Card>
  </>;
};
