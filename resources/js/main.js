var pdbFile = null;

window.lynxCBRV = {
    showInfo: () => {
      document.getElementById('info').innerHTML = NL_APPID + " is running on port " +
                  NL_PORT + " inside " + NL_OS + ".<br/><br/>" + "<span>v" + NL_VERSION + "</span>";
    },
    openDocs: () => {
      Neutralino.app.open({
        url: "https://neutralino.js.org/docs"
      });
    },
    checkPDB: async () => {
      div = document.getElementById("pdbNotify");
      if(pdbFile == null){
        div.innerHTML=`
        <div class="info-box warning col-12" style="position:relative;">
          <div class="info-box-content">
            Remember, it is necessary to select a PDB file in order to verify it.
          </div>
        </div>
        `
      }else{
        let com = 'python resources/scripts/verify.py '.concat(pdbFile);
        console.log(com);
        let response = await Neutralino.os.execCommand({
          command: com
        });
        let resp = JSON.parse(response.output);
        console.log(resp)
        if (resp.code == 200) {
          div.innerHTML=`
          <div class="info-box success col-12" style="position:relative;">
            <div class="info-box-content">
              Your PDB file appears to be fine, we can get on with it.
            </div>
          </div>
          `
        }else{
          div.innerHTML=`
          <div class="info-box alert col-12" style="position:relative;">
            <div class="info-box-content">
              `.concat(resp.response).concat(`
            </div>
          </div>
          `)
        }
      }
    },
    openPDB: async () => {
      let response = await Neutralino.os.showDialogOpen({
        title: 'Select Your PDB'
      });
      pdbFile = response.selectedEntry;
      setPathInfo();
    }
};

// Funciones

function setPathInfo(){
  div = document.getElementById("divFilePath");
  if (pdbFile) {
    div.value = pdbFile;
  }else{
    div.value = `You didn't select any file`;
  }
}

// Secuencia de inicio

Neutralino.init();
setPathInfo();
