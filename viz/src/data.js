// The exhibition's data: the checked records in date order (built from ../data by scripts/build-data.mjs).
export async function loadGazes() {
  const { gazes: all } = await (await fetch(`${import.meta.env.BASE_URL}gazes.json?v=${__DATA_VERSION__}`)).json();
  const gazes = all.filter((g) => g.voice_type !== 'self'); // Atatürk's words about himself are kept in the data, not shown here
  // a record that knows only its year (or its month) comes after the dated records of that year (or month):
  // "sometime in 1919" should not open the thread ahead of July 1919
  const when = (d) => (/^\d{4}$/.test(d) ? `${d}-99-99` : /^\d{4}-\d{2}$/.test(d) ? `${d}-99` : d);
  const byDate = [...gazes].sort((a, b) => (when(a.date) < when(b.date) ? -1 : when(a.date) > when(b.date) ? 1 : 0));
  byDate.forEach((g, i) => { g.rank = i; });
  return { gazes, byDate };
}
