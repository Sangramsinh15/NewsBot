import "./App.css";
import NavbarComp from "./Components/Navbar";
import { Grid, Box } from "@mui/material";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import { TextField } from "@mui/material";
import { Paper } from "@mui/material";
import { Button, Typography } from "@mui/material";
import { useEffect, useState } from "react";
import { myResults } from "./Components/Main Header";
import MessageCardComp from "./Components/MessageCard";
import axios from "axios";
import { myResponse } from "./Components/Main Header/index1";
import ResponseCardComp from "./Components/ResponseCardComp";
import GenreComp from "./Components/GenreComp";

const darkTheme = createTheme({
  palette: {
    mode: "dark",
  },
});

const sessionID = "1234"

function App() {
  const [searchKeyword, setSearchKeyword] = useState("");
  const [result, setResult] = useState({});
  const [tags, setTags] = useState([]);

  var mytags = [];

  const handleClick = async (e) => {
    const tempResult = {
      message: searchKeyword,
    };
    myResults.push(tempResult);

    var data = JSON.stringify({
      text: searchKeyword,
      session_id: sessionID,
    });

    var config = {
      method: "post",
      url: "http://44.200.109.25:80/get_response_1",
      headers: {
        "Content-Type": "application/json",
      },
      data: data,
    };

    await axios(config)
      .then(function(response) {
        console.log(JSON.stringify(response));
        const AIresponse = {
          message: response.data.message,
        };
        myResponse.push(AIresponse);
        mytags = response.data.tags;
      })
      .catch(function(error) {
        console.log(error);
        console.log(error.message);
        console.log(error.response);
        console.log(error.request);
      });
    setResult(tempResult);
    setTags(mytags);
    console.log(tags);
  };

  return (
    <ThemeProvider theme={darkTheme}>
      <Grid container spacing={0.5} justifyContent="center" alignItems="center">
        <Grid item xs={12}>
          <NavbarComp />
        </Grid>
        <Grid item xs={6}>
          <Grid container direction="column" sx={{ pt: 3 }} alignItems="center">
            {myResults.map((myVariable) => {
              return (
                <MessageCardComp
                  text={myVariable.message}
                  name={myVariable.name}
                />
              );
            })}
          </Grid>
        </Grid>
        <Grid item xs={6}>
          <Grid container direction="column" sx={{ pt: 3 }} alignItems="center">
            {myResponse.map((myVariable) => {
              return (
                <ResponseCardComp
                  text={myVariable.message}
                  name={myVariable.name}
                />
              );
            })}
          </Grid>
        </Grid>

        <Grid item xs={12}>
          <Grid
            container
            justifyContent="center"
            alignItems="center"
            spacing={{ xs: 2, md: 3 }}
            columns={{ xs: 4, sm: 8, md: 12 }}
            sx={{pt:4}}
          >
            {tags.map((myVar, index) => {
              return <GenreComp text={myVar} />;
            })}
          </Grid>
        </Grid>

        <Grid item xs={8}>
          <Grid container sx={{ pt: 3 }} alignItems="center">
            <Box
              component="span"
              sx={{
                fontSize: 16,
                fontFamily: "Arial",
                fontWeight: "bold",
                mr: 2,
              }}
            >
              Please Enter a Query
            </Box>
            <Box sx={{ flexGrow: 1, mr: 1 }}>
              <Paper>
                <TextField
                  id="searchKeyword"
                  name="searchKeyword"
                  type="search"
                  variant="filled"
                  onChange={(v) => setSearchKeyword(v.target.value)}
                  fullWidth
                />
              </Paper>
            </Box>
            <Button onClick={handleClick} variant="contained">
              <Typography p={1}>Search</Typography>
            </Button>
          </Grid>
        </Grid>
      </Grid>
    </ThemeProvider>
  );
}

export default App;
