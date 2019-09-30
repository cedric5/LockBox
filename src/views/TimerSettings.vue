<template>
<div class="timer-settings">
      <h2>{{ title }}</h2>              
      <h3>What time should the box close?</h3>
             <input type="datetime-local" id="close-time" name="close-time" value="2018-06-12T19:30" min="2018-06-07T00:00" max="2018-06-14T00:00">
             <br>
             <h3>What time should the box open?</h3>
             <input type="datetime-local" id="open-time" name="open-time" value="2018-06-12T19:30" min="2018-06-07T00:00" max="2018-06-14T00:00">
             <br>
             <button @click="clickHandler">Save</button>
</div>
</template>

<script>
export default {
  name: "timer-settings",
  props: {
    title: String
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h2 { 
    padding-top:25px;
    font-size: 2em;
    margin-top:0px;
 }
 h3 { 
     font-size: 1.5em;
     margin-top: 0px;
     }
.timer-settings{
     text-align: center; 
    }
.timer-settings button {
    width: 95%;
    max-width: 25em;
    margin-top:10px;
    cursor:pointer;
    overflow: hidden;
    outline:none;
}
</style>
