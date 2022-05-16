<template>
  <div class="hello">
    <h5>Url Shortener</h5>
    <span class="p-input-icon-right">
      <i class="pi pi-spin pi-spinner" />
      <InputText
        type="url"
        v-model="inputUrl"
        placeholder="Large"
        v-on:keyup.enter="submitUrl"
      />
      <h5>{{ validationMessage }}</h5>
      <h5 v-if="output.message">
        {{ output.message }} <br />
        {{ output.data }}
        <h2>
          <a href="output.url">{{ output.url }}</a>
        </h2>
      </h5>
    </span>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { ref } from "vue";

export default defineComponent({
  name: "HomePage",
  setup() {
    const frontendServerBaseUrl = process.env.VUE_APP_BASE_URL;
    const backendServerBaseUrl = process.env.VUE_APP_BACKEND_BASE_URL;
    const inputUrl = ref("");
    const output = ref({});
    const validationMessage = ref("");

    async function isURLValid(urlAddress: string) {
      validationMessage.value = "";
      try {
        new URL(urlAddress);
      } catch (e) {
        validationMessage.value = "Invalid URL: " + urlAddress;
        return false;
      }
      return true;
    }

    async function submitUrl() {
      output.value = {};
      if (await isURLValid(inputUrl.value)) {
        const submisisonUrl = [backendServerBaseUrl, "api/links/"].join("");
        const response = await fetch(submisisonUrl, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ url_address: inputUrl.value }),
        });
        let jsonValue = await response.json();

        if (response.status == 201) {
          output.value = {
            message: "Successfully created!",
            data: jsonValue,
            url: frontendServerBaseUrl + jsonValue.key + "/",
          };
        } else if (response.status == 409) {
          output.value = {
            message: "This Url is already in database!",
            data: jsonValue,
            url: frontendServerBaseUrl + jsonValue.key + "/",
          };
        } else {
          output.value = {
            message: "Status Code: " + response.status,
            data: jsonValue,
          };
        }
      }
    }

    return {
      submitUrl,
      inputUrl,
      output,
      validationMessage,
    };
  },
});
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
