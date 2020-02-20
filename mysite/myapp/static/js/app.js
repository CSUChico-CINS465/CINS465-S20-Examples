$(document).foundation()


var app4 = new Vue({
    el: '#app-4',
    data: {
      suggestions: [],
      seen:true,
      unseen:false
    },
    //Adapted from https://stackoverflow.com/questions/36572540/vue-js-auto-reload-refresh-data-with-timer
    created: function() {
          this.fetchSuggestionList();
          this.timer = setInterval(this.fetchSuggestionList, 10000);
    },
    methods: {
      fetchSuggestionList: function() {
          // $.get('/suggestions/', function(suggest_list) {
          //     this.suggestions = suggest_list.suggestions;
          //     console.log(suggest_list);
          // }.bind(this));
          axios
            .get('/suggestions/')
            // .then(response => console.log(response.data))
            .then(response => (this.suggestions = response.data.suggestions))
          console.log(this.suggestions)
          this.seen=false
          this.unseen=true
      },
      cancelAutoUpdate: function() { clearInterval(this.timer) }
    },
    beforeDestroy() {
      // clearInterval(this.timer)
      this.cancelAutoUpdate();
    }
  
  })