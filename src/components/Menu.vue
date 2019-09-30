<template>
<div class="menu">   
      <div class = "mdl-layout mdl-js-layout mdl-layout--fixed-drawer">
         <div class = "mdl-layout__drawer">
            <span class = "mdl-layout-title">Settings</span>
            <nav class = "mdl-navigation">
                <router-link to="/" class="mdl-navigation__link">Home</router-link>
                <router-link to="/timer-settings" class="mdl-navigation__link">Open and close settings</router-link>
                <router-link to="/wifi-settings" class = "mdl-navigation__link">Wifi Settings</router-link>
            </nav>
         </div>
      </div>
</div>
</template>
