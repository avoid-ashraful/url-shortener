<template>
  <div class="url-fetch">
    <h5>{{ urlFetchMessage }}</h5>
  </div>
  <div class="url-creation" v-if="!inputUrlKey">
    <h5>Url Shortener</h5>
    <span class>
      <InputText
        type="url"
        v-model="inputUrl"
        placeholder="Url"
        class="p-inputtext-lg"
        v-on:keyup.enter="submitUrl"
      />
      <h5>{{ validationMessage }}</h5>
      <h5 v-if="output.message">
        {{ output.message }} <br />
        {{ output.data }}
        <h2>
          <a v-bind:href="output.url">{{ output.url }}</a>
        </h2>
      </h5>
    </span>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
  name: "HomePage",
  setup() {
    const delay = (ms: number) => new Promise((res) => setTimeout(res, ms));

    const frontendServerBaseUrl = process.env.VUE_APP_BASE_URL;
    const backendServerBaseUrl = process.env.VUE_APP_BACKEND_BASE_URL;

    const urlFetchMessage = ref("");
    const inputUrl = ref("");
    const inputUrlKey = ref("");
    const output = ref({});
    const validationMessage = ref("");

    console.log(window.location.pathname);
    if (window.location.pathname.length > 1) {
      inputUrlKey.value = window.location.pathname.substring(1);
      getUrl();
    }

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
            url: frontendServerBaseUrl + jsonValue.key,
          };
        } else if (response.status == 409) {
          output.value = {
            message: "This Url is already in database!",
            data: jsonValue,
            url: frontendServerBaseUrl + jsonValue.key,
          };
        } else {
          output.value = {
            message: "Status Code: " + response.status,
            data: jsonValue,
          };
        }
      }
    }

    async function getUrl() {
      urlFetchMessage.value = "";
      const url = [backendServerBaseUrl, inputUrlKey.value].join("");
      const response = await fetch(url, {
        headers: {
          "Content-Type": "application/json",
        },
      });
      let jsonValue = await response.json();

      if (response.status == 200) {
        console.log(jsonValue);
        window.location.replace(jsonValue.url_address);
      } else {
        urlFetchMessage.value = "Your shorten url is not valid!";
        await delay(5000);
        window.location.replace("/");
        return;
      }
    }

    return {
      submitUrl,
      inputUrl,
      output,
      validationMessage,
      urlFetchMessage,
      inputUrlKey,
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
.url-creation {
  text-align: center;
}
.p-inputtext-lg {
  width: 75%;
}
</style>
