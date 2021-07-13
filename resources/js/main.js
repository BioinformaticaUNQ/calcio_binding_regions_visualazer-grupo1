var pdbFile = null;
const darkModIndicator = document.getElementById('darkIndicator');

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
        let com = 'python3 resources/scripts/verify.py '.concat(pdbFile);
        let response = await Neutralino.os.execCommand({
          command: com
        });
        let resp = JSON.parse(response.output);
        if (resp.code == 200) {
          div.innerHTML=`
          <div class="info-box success col-12" style="position:relative;">
            <div class="info-box-content">
              `.concat(resp.response).concat(`
            </div>
          </div>
          `)
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
    },
    openInPyMol : async () =>{
      let com = 'python3 resources/scripts/openPymol.py '.concat(pdbFile);
      let response = await Neutralino.os.execCommand({
        command: com
      });
    },
    clear : async () =>{
      await Neutralino.os.execCommand({
        command: 'python3 resources/scripts/clear.py'
      });
    },
    generateFasta: async () => {
      Metro.dialog.open("#fastaDialog");
      let com = 'python3 resources/scripts/getSecuencia.py '.concat(pdbFile);
      let response = await Neutralino.os.execCommand({
        command: com
      });
      console.log(response.output);
      Metro.dialog.close("#fastaDialog");
    },
    graficarFasta : async () =>{
      Metro.dialog.open("#graphicDialog");
      await Neutralino.os.execCommand({
        command: 'python3 resources/scripts/graficarFasta.py'
      });
      Metro.dialog.close("#graphicDialog");
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

function toggleDarkMode(){
  if (darkIndicator.checked) {
    document.documentElement.style.setProperty('--bg-color', 'rgba(0,0,0,0.8)');
    document.documentElement.style.setProperty('--font-color', '#FFF');
  }else {
    document.documentElement.style.setProperty('--bg-color', 'rgba(255,255,255,0.8)');
    document.documentElement.style.setProperty('--font-color', '#000');
  }
}

function changePrimaryColor(color){
  document.documentElement.style.setProperty('--primary-color', String(color));
}

// Secuencia de inicio
Neutralino.init();
setPathInfo();
window.lynxCBRV.clear();
