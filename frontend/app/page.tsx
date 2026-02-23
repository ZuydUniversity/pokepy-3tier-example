import Card from "./ui/Card";

async function getAllPokemon() {
  console.log("URL: ", process.env.NEXT_PUBLIC_BACKEND_URL)

  const url =
    process.env.NEXT_PUBLIC_BACKEND_URL! +
    process.env.NEXT_PUBLIC_BACKEND_API_PATH!;
  console.log("URL: ", url)

  if (!url) {
    throw new Error("Env not set");
  }
  const response = await fetch(url);

  if (!response.ok) {
    throw new Error("Failed to fetch data");
  }

  return response.json();
}

function addZeros(number: number) {
  let numStr = String(number);
  while (numStr.length < 3) {
    numStr = "0" + numStr;
  }

  return numStr;
}

function addSpaceBeforeUppercase(text: string) {
  return text.replace(/([A-Z])/g, " $1");
}

export default async function Home() {
  const data = await getAllPokemon();
  const randomPokemon = Math.floor(Math.random() * data.length) + 1;

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="z-10 w-full max-w-5xl items-center justify-between font-mono text-sm lg:flex">
        <div className="fixed bottom-0 left-0 flex h-48 w-full items-end justify-center bg-gradient-to-t from-white via-white dark:from-black dark:via-black lg:static lg:size-auto lg:bg-none"></div>
      </div>

      <Card
        body={"Generation " + data[randomPokemon - 1].Generation}
        title={addSpaceBeforeUppercase(data[randomPokemon - 1].Name)}
        image={
          "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/" +
          addZeros(data[randomPokemon - 1].Pokedex_Number) +
          ".png"
        }
        subtitle={"Main type " + data[randomPokemon - 1].Type_1}
        // btn={{
        //   text: "Click",
        //   href: "#",
        //   filled: false,
        //   type: "primary",
        //   icon: <PaperAirplaneIcon />
        // }}
      />
    </main>
  );
}
