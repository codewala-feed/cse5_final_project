const inpTag = document.getElementsByTagName("input")
const selectTag = document.getElementsByTagName("select")

function onShadow(TagName){
    for (let index = 0; index < TagName.length; index++) {
        const element = TagName[index];
        element.addEventListener("mouseenter", function(){
            element.style.boxShadow = "4px 4px 8px aliceblue";
        })
    
        element.addEventListener("mouseleave", function(){
            element.style.boxShadow = "";
        })
    }
}

onShadow(inpTag)
onShadow(selectTag)