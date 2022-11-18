
var x = []
var y = []



const FollowerCounter = (data) => {

    $('#loader2').removeClass('block')
    $('#loader2').addClass("hidden")
    $('#followercounter').removeClass('hidden')
    $('#followercounter').addClass('block')
    $('#followerQuantity').selectedElement.innerText = data.Follower[0]


}

const Graph = (jsonData) => {

    $('#graph').removeClass('hidden')
    $('#graph').addClass('block')
    $('#loader').removeClass('block')
    $('#loader').addClass('hidden')
    Object.keys(jsonData).forEach(element => {
        x.push(jsonData.Date)
        y.push(jsonData.Follower)
    });
    
    var data = [{
        x:Object.values(x[0]),
        y:Object.values(y[0]),
        mode: 'lines'
    }]


   
    
    Plotly.newPlot($('#graph').selectedElement, data) 
}

function $(selector) {
    /* Select elements of selected id, class */
    const selected = document.querySelector(selector)
  
    /* Return methods and attributes of selected elements*/
  
    return {
      selectedElement: selected,
      getClassList: [...selected.classList.values()],
      setClassList: function(ListOfClass) {
        selected.classList = ListOfClass.join(" ")
      },
      addClass: function(AddingClass) {
        const added = [...this.getClassList, AddingClass]
        this.setClassList(added)
      },
      removeClass: function(removingClass) {
        const removed = this.getClassList.filter((value) => removingClass != value)
        this.setClassList(removed)
      },
      addListener: (listener, type = "click") => selected.addEventListener(type, listener)
    }
  }

const request = fetch('pandas_to_json.json')
.then((response) => response.json())
.then((json) => {
   let jsonData = json
   setTimeout(() => {
    Graph(jsonData)
   }, "3000")
   
})

const request2 = fetch('Follower.json')
.then((response) => response.json())
.then((json)=> {
    let followerJsonData = json
    setTimeout(()=> {
        FollowerCounter(followerJsonData)
    },"3000")
})