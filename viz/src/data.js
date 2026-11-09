// The exhibition's data: the checked records in date order (built from ../data by scripts/build-data.mjs).
export async function loadGazes() {
  const { gazes: all } = await (await fetch(`${import.meta.env.BASE_URL}gazes.json?v=${__DATA_VERSION__}`)).json();
  const gazes = all.filter((g) => g.voice_type !== 'self'); // Atatürk's words about himself are kept in the data, not shown here
  const byDate = [...gazes].sort((a, b) => a.date.localeCompare(b.date));
  byDate.forEach((g, i) => { g.rank = i; });
  return { gazes, byDate };
}
