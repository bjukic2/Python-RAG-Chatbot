import { askChatbot } from "./api/chat/route";

export default async function Page() {
  const data = await askChatbot("Hello");
  return <div>{data.answer}</div>;
}
