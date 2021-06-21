// run this in your terminal:
// $ cargo init
// $ cargo build
// $ cargo run

// Cargo.toml
/*

[package]
name = "basicmonolith"
version = "0.1.0"
authors = ["Me"]
edition = "2021"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
rocket = "0.4.10"

[dependencies.rocket_contrib]
version = "0.4.10"
default-features = true

*/

// put this in your src/main.rs
#![feature(proc_macro_hygiene, decl_macro)]

#[macro_use] extern crate rocket;

use rocket_contrib::serve::StaticFiles;

fn main() {
    rocket::ignite()
        .mount("/hello/world", StaticFiles::from("./public"))
        .launch();
}