<template>
    <div id="child">
        <h2>Child</h2>
        <input v-model='childData'
        @input="onInput" 
        type="text"
        >

        <p>parentData: {{ parentData }}</p>
        <p>grandParentData: {{ grandParentData }}</p>
    </div>
</template>

<script>
export default {
    name: 'Child',
    props: {
        grandParentData: {
            type: String,
        },
        parentData: {
            type: String,
        },
    },
    data: function () {
        return {
            childData: '',
        }
    },
    methods: {
        onInput: function () {
            // console.log('수정사항발생!')
            this.$emit('child-input', this.childData)
        },
    },
}
</script>

<style>
#child {
    border: 2px solid darkblue;
    margin: 1rem;
}
</style>