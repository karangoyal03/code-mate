<script>
  import {
    Navbar,
    NavBrand,
    NavLi,
    NavUl,
    NavHamburger,
    Avatar,
    Dropdown,
    DropdownItem,
    DropdownHeader,
    DropdownDivider,
    Button,
  } from "flowbite-svelte";
  import { ChevronDownOutline } from "flowbite-svelte-icons";
</script>

<Navbar class="bg-[#0076CE]">
  <NavBrand href="/">
    <span
      class="self-center whitespace-nowrap text-xl font-extrabold text-white"
      >Code-Mate</span
    >
  </NavBrand>
  <div class="flex items-center md:order-2">
    <Avatar id="avatar-menu">KG</Avatar>
  </div>
  <Dropdown placement="bottom" triggeredBy="#avatar-menu">
    <DropdownHeader>
      <span class="block text-sm">Current user</span>
      <span class="block truncate text-sm font-medium"
        >currentuser@email.com</span
      >
    </DropdownHeader>
    <DropdownDivider />
    <DropdownItem>Sign out</DropdownItem>
  </Dropdown>
</Navbar>
