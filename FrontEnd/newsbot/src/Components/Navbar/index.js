import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import { Grid } from '@mui/material';

const NavbarComp = () => {

  return (
    <AppBar position="static">
      <Grid container maxWidth="xl" justifyContent="center" alignItems="center">
        <Toolbar disableGutters>
          <Typography
            variant="h3"
            noWrap
            component="a"
            href="/"
            sx={{
              mr: 2,
              display: { xs: 'none', md: 'flex' },
              fontFamily: 'monospace',
              fontWeight: 700,
              letterSpacing: '.3rem',
              color: 'inherit',
              textDecoration: 'none',
            }}
          >
            NewsBot
          </Typography>
        </Toolbar>
      </Grid>
    </AppBar>
  );
};
export default NavbarComp;